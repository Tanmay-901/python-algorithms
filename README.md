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
## **Odd-Even:**O(1)  
```python
if n&1 == 1:
    print('odd')
else:
    print('even')
```
## **Leftshift(multiply) / Rightshift(divide) by 2<sup>n</sup>:**O(1)  
```python
def multpow(x,y):
    return x<<y  # x*(2^y)
def divpow(x,y):
    return x>>y # x/(2^y)
```
## **Check if a number is power of 2:**O(1)  
```python
def ispow(n):
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y
```
## **count 1's in binary representation:**O(log(n))  
```python''
def cntbits(n):
    cnt = 0
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt
```
