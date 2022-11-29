# A very easy way to render block matrices in LaTeX

You've probably seen this before: a block matrix in LaTeX. It's a pain to write, and it's even more of a pain to read.
I've personally been in this situation many times, and I've always found myself wishing there was a better way to do it.
Whoever you are, this is for you !

First step is always to clone the repository:

```bash
git clone https://github.com/arnos-stuff/gen.git
```

Don't forget that github [now has an annoying token authentification system](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories), but i'm sure you can figure it out.
Then, here's what's in store for now:

## How to use it

This isn't a package (yet), so you'll have to import the code locally after cloning this repo into your document.

```python
from blockMatSymbol import blockMatSymbolAsSqBlocks, matrixSymbolAsRowVectors, matrixSymbolAsColVectors
```

```python
import sympy as sp
```


```python
n,m = sp.symbols('n, m', integer=True, positive=True) # matrix dimensions
```
The most basic thing you could do is to render a block matrix as a bunch of column or row vectors.

```python
cA = matrixSymbolAsColVectors('A', n, m)
```

Using the latex interpreter that's baked into sympy, we can get latex that the jupyter notebook can render.

```python
cA
```

$$\left[\begin{matrix}a_{1} & \dots & a_{j} & \dots & a_{m}\end{matrix}\right]$$

Impressive no ? What about a row vector decomposition ?

```python
rA = matrixSymbolAsRowVectors('A', n, m)
```

Let's see what we've got here:

```python
rA
```

$$\left[\begin{matrix}\tilde{a}_1^T\\
\vdots\\
\tilde{a}_i^T\\
\vdots\\
\tilde{a}_n^T\end{matrix}\right]$$

Alright, so now we can render a block matrix as a bunch of row or column vectors. The least we can ask is that the dimensions are correct, right ?

```python
assert rA.shape == cA.shape
```
This doesn't fail because the dimensions are correct !

```python
rA.shape
```




    (n, m)






Okay, so now we can render using vectors. But what if we want to render it as a bunch of square blocks ?

```python
bmA = blockMatSymbolAsSqBlocks('A', subsize=n)
```
Here we go :scream:

```python
bmA
```

$$\left[\begin{matrix}A_{1,1} & \dots & A_{1,j} & \dots & A_{1,m}\\
\vdots & \ddots & \vdots & \ddots & \vdots\\
A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\\
\vdots & \ddots & \vdots & \ddots & \vdots\\
A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\end{matrix}\right]$$

**WOAH**. That's a lot of blocks. But what if we want to avoid the clutter ? Removing the diagonal dots its an option :smile:

```python
bmA = blockMatSymbolAsSqBlocks('A', subsize=n, nodiag=True)
# no diagonal blocks displayed
```
Last but not least ..
```python
bmA
```

$$\left[\begin{matrix}A_{1,1} & \dots & A_{1,j} & \dots & A_{1,m}\\
\vdots &   & \vdots &   & \vdots\\
A_{i,1} & \dots & A_{i,j} & \dots & A_{i,m}\\
\vdots &   & \vdots &   & \vdots\\
A_{n,1} & \dots & A_{n,j} & \dots & A_{n,m}\end{matrix}\right]$$

Here we go :rocket:

## A note

This was generated using the notebook `demo.ipynb` in the repo. You can find it [here](demo.ipynb).

You can turn any notebook into a markdown file using the following command:

```bash
jupyter nbconvert --to markdown demo.ipynb
```

## How to contribute

I'm not a LaTeX expert, so if you have any suggestions, feel free to open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Future work

- [x] Barebones implementation
- [ ] Add a package
- [ ] Add a way to ouput pure LaTeX code
- [ ] Add a markdown to LaTeX converter
- [ ] Add a txt/csv to LaTeX converter
- [ ] Have some command line interface
- [ ] Maybe have some supports from [sympy](https://www.sympy.org/en/index.html) itself ??