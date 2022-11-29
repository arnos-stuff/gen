```python
from blockMatSymbol import blockMatSymbolAsSqBlocks, matrixSymbolAsRowVectors, matrixSymbolAsColVectors
```


```python
import sympy as sp
```


```python
n,m = sp.symbols('n, m', integer=True, positive=True) # matrix dimensions
```


```python
cA = matrixSymbolAsColVectors('A', n, m)
```


```python
cA
```




$\displaystyle \left[\begin{matrix}a_{1} & \dots & a_{j} & \dots & a_{m}\end{matrix}\right]$




```python
rA = matrixSymbolAsRowVectors('A', n, m)
```


```python
rA
```




$\displaystyle \left[\begin{matrix}\tilde{a}_1^T\\\vdots\\\tilde{a}_i^T\\\vdots\\\tilde{a}_n^T\end{matrix}\right]$




```python
assert rA.shape == cA.shape
```


```python
rA.shape
```




    (n, m)




```python
bmA = blockMatSymbolAsSqBlocks('A', subsize=n)
```


```python
bmA
```




$\displaystyle \left[\begin{matrix}A_{1,1} & \dots & A_{1,j} & \dots & A_{1,m}\\\vdots & \ddots & \vdots & \ddots & \vdots\\A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\\\vdots & \ddots & \vdots & \ddots & \vdots\\A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\end{matrix}\right]$




```python
bmA = blockMatSymbolAsSqBlocks('A', subsize=n, nodiag=True) # no diagonal blocks displayed
```


```python
bmA
```




$\displaystyle \left[\begin{matrix}A_{1,1} & \dots & A_{1,j} & \dots & A_{1,m}\\\vdots &   & \vdots &   & \vdots\\A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\\\vdots &   & \vdots &   & \vdots\\A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\end{matrix}\right]$


