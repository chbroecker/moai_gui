# moai_gui

## Python Requirements
* Python3
* PySide2

## Preprocessing
Because string comparison is costly we map the item strings to integers. We are then able to calculate a solution faster
and map the solution back to the actual item names.

```
Unserialized PSUs:                                                                                                                                                    
{1: ['i1', 'i4', 'i8'], 2: ['i2', 'i3', 'i4'], 3: ['i1', 'i5', 'i8'], 4: ['i6', 'i7'], 5: ['i2', 'i7', 'i8']}                                                         
Serialized PSUs:                                                                                                                                                      
{1: [0, 3, 7], 2: [1, 2, 3], 3: [0, 4, 7], 4: [5, 6], 5: [1, 6, 7]}
```

After the serialization step we filter the PSUs further. To find a solution we only have to look at the PSUs that contain
items that are in our order. 
We can also go ahead and ignore all items that are on these interesting PSUs but that are also not in our order.

```
Order:                                                                                                                                                                
[0, 2, 3]                                                                                                                                                             
Original PSUs:                                                                                                                                                        
{1: [0, 3, 7], 2: [1, 2, 3], 3: [0, 4, 7], 4: [5, 6], 5: [1, 6, 7]}                                                                                                   
Filtered PSUs:                                                                                                                                                        
{1: [0, 3], 2: [2, 3], 3: [0]}
```

The resulting Filtered PSU has a lot less items and should therefore be a lot more suitable for the search algorithms
