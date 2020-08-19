# **python-algorithms**
## efficient algorithms for general tasks with good time complexity.

------------------------------------------------------------------------------------

## **Referance:** [Competetive programming with python](https://www.youtube.com/playlist?list=PLS1QulWo1RIZZc0V_a8cEuFFkF5KbGlsf)

------------------------------------------------------------------------------------
####bitwise operator not - ~
####bitwise operator xor - ^
####bitwise operator rightshift - >>
####bitwise operator leftshift - <<

-------------------------------------------------------------------------------------
##**Odd-Even: **
```python
if n&1 == 1:
    print('odd')
else:
    print('even')
```
##**Multiply/Divide with power of 2^n: **
````python
def multpow(x,y):
    return x<<y  # x*(2^y)
def divpow(x,y):
    return x>>y # x/2^y
```
