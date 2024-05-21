====================================================
EXT: Mu editor
====================================================

| Mu editor is the simplest choice of windows apps to use when programming the microbit with micropython.
| However, it can lag behind the latest version of micropython.
| For more recent features it may be better to use the online simulator at https://python.microbit.org/v/3. This uses the latest micropython for the latest version of the microbit.

----

Installing at school
--------------------------

#. Do a windows search for ``Software centre`` and open it.
#. Search for Mu.
#. Install Mu editor.

----

First use
--------------------------

#. Click the **Mode** icon and set the mode to **BBC micro:bit**.
#. Create a new file and save it in a folder called "DigiStem".
#. Create code for the microbit then click **Check** to check for any errors.
#. To put code onto the microbit, connect it via USB then click the **Flash** icon.

----

Keyboard shortcuts
--------------------------

Useful keyboard shortcuts are at: https://codewith.mu/en/tutorials/1.2/shortcuts

| **Microbit**
=============  ======================================================================
 Keys          Action
=============  ======================================================================
 F3            Flash code onto device (the same as clicking "Flash").
=============  ======================================================================

| **Text Editing**
=============  ======================================================================
 Keys          Action
=============  ======================================================================
 CTRL F        Show the find and replace dialog.
 CTRL K        Toggle comments for the current or selected lines of code.
 TAB           Indent the current or selected lines by four spaces.
 SHIFT TAB     Unindent the current or selected lines by four spaces.
 CTRL Z        Undo (keep pressing to keep undoing).
 CTRL Y        Redo (keep pressing to keep redoing).
 CTRL A        Select all
 CTRL X        Cut selected text into the clipboard.
 CTRL C        Copy selected text into the clipboard.
 CTRL V        Paste text from the clipboard.
 CTRL SHIFT S  Save the current tab with a new name (or double click the tab's name).
=============  ======================================================================

----

Fixing indenting quickly
--------------------------

| Select multiple lines of code.
| Unindent them all at once using ``SHIFT TAB``.
| Indent them all at once using ``TAB``

.. image:: images/multi_line_indent_moving.gif
    :scale: 75 %
    :align: center

----

.. admonition:: Questions

    #. What is the shortcut to toggle comments?
    #. What is the shortcut to increase the indent of selected lines?
    #. What is the shortcut to decrease the indent of selected lines?
    #. What is the shortcut to select all the text?


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                What is the shortcut to toggle comments?
                Ctrl: K
    
            .. tab-item:: Q2

                What is the shortcut to increase the indent of selected lines?
                TAB

            .. tab-item:: Q3

                What is the shortcut to decrease the indent of selected lines?
                SHIFT TAB
    
            .. tab-item:: Q4

                What is the shortcut to select all the text?
                Ctrl: A

----

Mu editor Errors
-----------------------

| For examples see the Errors section.
| https://pc-microbit-micropython.readthedocs.io/en/latest/errors/Types_of_Errors.html

| Working out what has gone wrong and how to fix it is a key part of everyday programming.
| Some errors will show up using the **check** button.
| Some errors will not show up using the **check** button, but instead, will be scrolled on the microbit as an error message when the microbit is flashed. They contain the line number for where you should start to identify and fix the issue.


----

Downloads
--------------------------

The latest version is at: https://codewith.mu/en/download
