# src/framework/util/matrix.h

```cpp
void setIdentity();
```
```cpp
bool isIdentity();
```
```cpp
void fill(T value);
```
```cpp
out << mat(i,j);
```
```cpp
in >> mat(i,j);
```
```cpp
public: Matrix();
```
```cpp
template<typename U> Matrix(const std::initializer_list<U>& values);
```
```cpp
template<typename U> Matrix(const U *values);
```
```cpp
T& operator()(int row, int column);
```
```cpp
std::ostream& operator<<(std::ostream& out, const Matrix<N,M,T>& mat);
```
```cpp
std::istream& operator>>(std::istream& in, Matrix<N,M,T>& mat);
```