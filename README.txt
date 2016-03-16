# Wearables data merge task


## How To Run The Code

On a linux plaform, cd into the "cpnp" directory if not in it already, and run "python merge.py" or just "./merge.py". Follow the prompts.

## Assumptions Made

Real-life datasets would be orders of magnitude larger.
More accurate timestamps may be available.
The CSV input files and the target database are hard-coded into the program for the purposes of this test, a live application would allow these to be chosen by the user.

## Data Quality Issues

Timestamp precision is only to the nearest minute and should be much more precise.
The frequency of samples for the accelerometer is very low and possibly too infrequent to be useful.
Much of the data supplied does not overlap chronologically, leading to a smaller useful dataset.
Some of the accelerometer data may not be useful, e.g. temp, and possilby clipsBeforeCalibr, clipsAfterCalibr

## Other Thoughts

In attempting this task, I found the Pandas Data Analysis library (http://pandas.pydata.org/), which I was not previously aware of, and that I think would be appropriate for this task. As well as providing many data analyis tools, it is optimized for performance (parts of it are written in Cython or C) and I expect it would perform significantly faster than hand-rolled python code.

### installing pandas

sudo pip install pandas
if this error is encountered: "SystemError: Cannot compile 'Python.h'. Perhaps you need to install python-dev|python-devel.", then do:
sudo apt-get install python-dev
then
sudo pip install pandas
(this takes rather a long time to compile...)


Chris Bird Wed Oct 28 14:59:49 2015

---
