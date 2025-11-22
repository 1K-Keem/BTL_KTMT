# Task 2.2 - 2 hàm solveLinearSystem, applyWienerFilter

```c++
// Giải hệ phương trình tuyến tính bằng Gauss elimination
void solveLinearSystem(double A[MAX_SIZE][MAX_SIZE], double b[MAX_SIZE], double x[MAX_SIZE], int N)
{
    // TODO
}

// Áp dụng Wiener filter
void applyWienerFilter(double input[MAX_SIZE], double coefficients[MAX_SIZE], double output[MAX_SIZE], int N)
{
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
0.9115744 0.07941656 2.2789361 2.7509499
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
1.1174561 -0.025610173 0.005156662 1.3409474 2.762908 3.2945309
```