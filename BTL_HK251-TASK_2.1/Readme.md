# TASK 2.1 - 3 hàm computeAutocorrelation, computeCrosscorrelation, và createToeplitzMatrix

```c++
// Tính autocorrelation của signal
void computeAutocorrelation(double signal[MAX_SIZE], double autocorr[MAX_SIZE], int N) {
    // TODO
}

// Hàm tính crosscorrelation giữa desired signal và input signal
void computeCrosscorrelation(double desired[MAX_SIZE], double input[MAX_SIZE], double crosscorr[MAX_SIZE], int N) {
    // TODO
}

// Hàm tạo ma trận Toeplitz từ autocorrelation
void createToeplitzMatrix(double autocorr[MAX_SIZE], double R[MAX_SIZE][MAX_SIZE], int N) {
    // TODO
}
```

## Run code

### Chạy với data1 `Bài toán Bộ lọc Wiener với d = [2.0, 3.0], x = [2.5, 2.8]` (trong latex)

```sh
.include "data1.asm"
# .include "data2.asm"
```

```sh
java -jar Mars45.jar nc main.asm

# result
root@32854dede839:/workspaces/template# java -jar Mars45.jar nc main.asm 
Data 1 - VOTIEN_KTMT_HK251: 
6.7 3.75 7.045 3.5 7.045 3.5 3.5 7.045 
```

### Chạy với data1 `Bài toán Bộ lọc Wiener với d = [1.5, 2.8, 3.2], x = [1.2, 2.5, 3.0], M = 3` (trong latex)

```sh
# .include "data1.asm"
.include "data2.asm"
```

```sh
java -jar Mars45.jar nc main.asm

# result
root@32854dede839:/workspaces/template# java -jar Mars45.jar nc main.asm 
Data 2 - VOTIEN_KTMT_HK251: 
6.1333337 3.7866669 1.2800001 5.5633335 3.5 1.2 5.5633335 3.5 1.2 3.5 5.5633335 3.5 1.2 3.5 5.5633335
```