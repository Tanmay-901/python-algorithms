# **Python-algorithms**  
## efficient algorithms for general tasks with good time complexity.  

------------------------------------------------------------------------------------

## **Referance:** [Competetive programming with python](https://www.youtube.com/playlist?list=PLS1QulWo1RIZZc0V_a8cEuFFkF5KbGlsf)  

------------------------------------------------------------------------------------
#### bitwise operator not - ~  
#### bitwise operator xor - ^  
#### bitwise operator rightshift - >>  
#### bitwise operator leftshift - <<  

-------------------------------------------------------------------------------------
## **Odd-Even:**  
```python
if n&1 == 1:
    print('odd')
else:
    print('even')
```
## **Multiply/Divide with power of 2<sup>n</sup>:**
````python
def multpow(x,y):
    return x<<y  # x*(2<sup>y</sup>)
def divpow(x,y):
    return x>>y # x/2<sup>y</sup>
```  
## **Check if a number is power of 2:**  
```python
def ispow(n):
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y
```
