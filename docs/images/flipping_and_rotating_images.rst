====================================================
Flipping and Rotating images
====================================================

| Custom functions are needed to flip or rotate images.

| To get the pixel data, use the **repr** function on the image object.


.. py:function:: repr(image)

    | Get a compact string representation of the image.

| In the code example below, the **repr** for the DUCK image is printed.
| Image('09900:99900:09999:09990:00000:')

.. code-block:: python
    
    from microbit import *
    
    img1 = Image.DUCK
    img_repr = repr(img1)
    print(img_repr)
    # Image('09900:99900:09999:09990:00000:')

| The next step is to collect just the numbers from the string, then put the numbers in a list format that can then be used to create an image using bytearray.

| The string can be sliced to ignore the first 6 characters and the last 3 characters
| This is done using **img_repr[7:-3]**.
| Then the colon is removed using the replace method.
| Finally, list comprehension is used on the string to converst each string numeral to an int in a list.
| This produces the list for a DUCK: [0, 9, 9, 0, 0, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0]

.. code-block:: python
    
    from microbit import *

    img_str = img_repr[7:-3]
    img_str = img_str.replace(":", "")
    img_array = [int(x) for x in img_str]

| So far the code has gone from 
| **Image.DUCK** 
| to 
| **Image('09900:99900:09999:09990:00000:')** 
| to 
| **[0, 9, 9, 0, 0, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0]**.

| Now functions need to be created for:
* flipping horizontally
* flipping vertically
* rotating 90 degrees clockwise or 90 anticlockwise.

