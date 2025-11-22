import numpy as np
import matplotlib.pyplot as plt

def read_signal(filename):
    """Đọc tín hiệu từ file"""
    with open(filename, 'r') as f:
        content = f.read()
        
        # Bỏ qua dòng "Filtered output:" và "MMSE:" nếu có
        lines = content.split('\n')
        numbers = []
        
        for line in lines:
            if line.startswith('Filtered output:'):
                # Lấy số từ dòng này
                parts = line.replace('Filtered output:', '').strip().split()
                numbers.extend([float(x) for x in parts])
            elif line.startswith('MMSE:'):
                # Bỏ qua dòng MMSE
                continue
            elif line.startswith('Error:'):
                # Trường hợp lỗi
                return None, line
            else:
                # Đọc số từ dòng thông thường
                parts = line.strip().split()
                for part in parts:
                    try:
                        numbers.append(float(part))
                    except:
                        pass
        
        return np.array(numbers), None

def extract_mmse(filename):
    """Trích xuất giá trị MMSE từ file output"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            for line in content.split('\n'):
                if line.startswith('MMSE:'):
                    return float(line.replace('MMSE:', '').strip())
    except:
        pass
    return None

def plot_weiner_filter():
    desired, _ = read_signal('desired.txt')
    input_signal, error = read_signal('input.txt')
    output, _ = read_signal('expected.txt')
    mmse = extract_mmse('expected.txt')

    # Kiểm tra lỗi
    if error:
        print(f"Lỗi: {error}")
        exit()

    # Tạo trục thời gian
    n_desired = len(desired)
    n_input = len(input_signal)
    n_output = len(output)

    print(f"Desired signal: {n_desired} samples")
    print(f"Input signal: {n_input} samples")
    print(f"Output signal: {n_output} samples")
    if mmse:
        print(f"MMSE: {mmse:.2f}")

    # Tạo figure với nhiều subplots
    fig = plt.figure(figsize=(16, 12))

    # 1. Đồ thị tín hiệu mong muốn (Desired Signal)
    ax1 = plt.subplot(4, 2, 1)
    plt.plot(desired, 'b-', linewidth=1, label='Desired Signal')
    plt.title('Desired Signal (Original)', fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 2. Đồ thị tín hiệu đầu vào có nhiễu (Input Signal)
    ax2 = plt.subplot(4, 2, 2)
    plt.plot(input_signal, 'r-', linewidth=0.8, alpha=0.7, label='Input Signal (Noisy)')
    plt.title('Input Signal (Desired + Noise)', fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 3. Đồ thị tín hiệu đầu ra sau lọc (Output Signal)
    ax3 = plt.subplot(4, 2, 3)
    plt.plot(output, 'g-', linewidth=1, label='Output Signal (Filtered)')
    plt.title('Output Signal (After Wiener Filter)', fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 4. So sánh Desired vs Output
    ax4 = plt.subplot(4, 2, 4)
    min_len = min(len(desired), len(output))
    plt.plot(desired[:min_len], 'b-', linewidth=1.5, label='Desired', alpha=0.7)
    plt.plot(output[:min_len], 'g--', linewidth=1.5, label='Output (Filtered)', alpha=0.7)
    plt.title('Comparison: Desired vs Output', fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 5. So sánh cả 3 tín hiệu (zoom vào 100 samples đầu)
    ax5 = plt.subplot(4, 2, 5)
    zoom_range = 100
    min_len_all = min(len(desired), len(input_signal), len(output), zoom_range)
    plt.plot(desired[:min_len_all], 'b-', linewidth=2, label='Desired', alpha=0.8)
    plt.plot(input_signal[:min_len_all], 'r-', linewidth=1, label='Input (Noisy)', alpha=0.5)
    plt.plot(output[:min_len_all], 'g--', linewidth=2, label='Output (Filtered)', alpha=0.8)
    plt.title(f'All Signals Comparison (First {min_len_all} Samples)', fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 6. Sai số giữa Desired và Output
    ax6 = plt.subplot(4, 2, 6)
    error_signal = desired[:min_len] - output[:min_len]
    plt.plot(error_signal, 'purple', linewidth=0.8, label='Error')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.title(f'Error: Desired - Output (MMSE: {mmse:.2f})' if mmse else 'Error: Desired - Output', 
            fontsize=12, fontweight='bold')
    plt.xlabel('Sample Index (n)')
    plt.ylabel('Error Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 7. Histogram của sai số
    ax7 = plt.subplot(4, 2, 7)
    plt.hist(error_signal, bins=50, color='purple', alpha=0.7, edgecolor='black')
    plt.title('Error Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Error Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3, axis='y')

    # 8. Spectral Power (FFT) - So sánh
    ax8 = plt.subplot(4, 2, 8)
    # FFT của desired
    fft_desired = np.abs(np.fft.fft(desired[:min_len]))[:min_len//2]
    # FFT của output
    fft_output = np.abs(np.fft.fft(output[:min_len]))[:min_len//2]
    # FFT của input
    fft_input = np.abs(np.fft.fft(input_signal[:min_len]))[:min_len//2]

    freq = np.fft.fftfreq(min_len)[:min_len//2]
    plt.plot(freq, fft_input, 'r-', linewidth=0.8, alpha=0.5, label='Input (Noisy)')
    plt.plot(freq, fft_desired, 'b-', linewidth=1.5, alpha=0.7, label='Desired')
    plt.plot(freq, fft_output, 'g--', linewidth=1.5, alpha=0.7, label='Output (Filtered)')
    plt.title('Frequency Spectrum Comparison', fontsize=12, fontweight='bold')
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Magnitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.yscale('log')

    plt.tight_layout()
    plt.savefig('wiener_filter_analysis.png', dpi=300, bbox_inches='tight')
    print("\nĐã lưu đồ thị vào file: wiener_filter_analysis.png")
    # plt.show()

if __name__ == "__main__":
    plot_weiner_filter()