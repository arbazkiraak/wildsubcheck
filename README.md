wildsubcheck - Filtering wildcard enabled subdomains from list 

# Workflow:

```
wildsubcheck [SCAN_TYPE] [SUBDOMAIN/SUBDOMAIN_LIST] OFFSET
```

* Offset is the value which compare list of response lengths `max_wildcard_len - sub_wildcard_len <= OFFSET` 
* Keep the offset value somewhere btw 70 to 120, it may depends of different domains.

# USAGE:

> SINGLE SUBDOMAIN:

![1](https://user-images.githubusercontent.com/13177578/64770100-27a6c000-d56a-11e9-859e-209d900d51a6.PNG)

> SUBDOMAIN LIST:

`wildsubcheck list subdomains.lst 100`

![2](https://user-images.githubusercontent.com/13177578/64770099-270e2980-d56a-11e9-8505-cc5c2b91b562.PNG)


# MISC:

* Filter Valid from the list :

```
→ wildsubcheck list subdomains.lst 100 | grep "VALID:" | cut -d ':' -f2
```

--------------------------------------

Note : (Just Another Rough Script  ¯\_(ツ)_/¯)
