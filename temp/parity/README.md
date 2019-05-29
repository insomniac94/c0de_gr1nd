# Computing the Parity of a Word

"Parity checks are used to detect single bit errors in data storage and communication." - EPI  

Problem:  
The parity of a binary word is 1 if the number of 1s in the word is odd. Conversely, the parity of a binary word is 0 if the number of 1s in the word is even. How would you compute the parity of a very large number of 64-bit words?   
  
Examples:  
```
1011   -> 1  
1001   -> 0  
100100 -> 0  
111000 -> 1  
```  
  
Solution - from [parity-mysol.py](parity-mysol.py):  
```python
def parity(x):
    result = 0
    while x:
        result = not result
        x = x & (x - 1)
    return int(result)
```  
  
Explanation:
1. Initialize parity = 0  
2. Loop while x != 0  
    a. Invert parity   
    ```python
    result = not result
    ```  
    b. Erase lowest (rightmost) set bit   
    ```python
    x = x & (x - 1)
    ```  
3. Return the parity  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)