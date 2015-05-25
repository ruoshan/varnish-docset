## how to generate the docset

Download the varnish [source code](https://repo.varnish-cache.org/source/varnish-4.0.3.tar.gz),
extract the archive, and do the old-school `./configure; make`;

the `doc` is under the directory `doc/sphinx/build/html`, but I would prefer the search box is removed.
change the file `doc/sphinx/conf.py`, find the option `html_sidevars`, change it to:

```
html_sidebars = { "**" : ["globaltoc.html", "localtoc.html", "relations.html"] }
```

and rebuild the document:

```
cd doc/sphinx
sphinx -b html . build/html-new
cp -r build/html-new varnish-docset/Documents
```

now you get the documents, call `python gen.py` to get the docSet.dsidx


## Status

currently, only some vcl related variables and subroutine are indexed. the document isn't organiszed
for parsing :(
