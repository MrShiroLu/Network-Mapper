# Network-Mapper

## To-Do
- [x] Resource
- [ ] GUI
- [x] Backend 

#### Nmap
- Scan result

```python
    scan_result["scan"][host][proto][port] = {
        "state": state,
        "reason": reason,
        "name": name,
        "product": product,
        "version": version,
        "extrainfo": extrainfo,
        "conf": conf,
        "cpe": cpe,
    }
```