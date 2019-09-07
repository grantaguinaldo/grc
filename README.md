# 2019 GRC API

The data for this API was obtained from `https://www.socalgas.com/regulatory/A17-10-008.shtml`. The pdf files from this website were downloaded and parsed using the [`PyPDF2`](https://pypi.org/project/PyPDF2/) library.

To use this API, you'll need to make a `GET` request using the format provided below.

`https://grc-api.herokuapp.com/api?fileidx=<'file_index'>`

To get the list of `fileidx` that are available, you can view all of the file indices by clicking [here](https://github.com/grantaguinaldo/grc/blob/master/misc/grc_2016_file_index.csv).

As an example, if you're trying to get file_index <code>2016000</code>, your complete end point will be:

`https://grc-api.herokuapp.com/api?fileidx=2016000`

This is a work in progress, and I will be adding to this API over time.
