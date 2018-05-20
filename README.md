# Romanize 3

Python 3 transliteration module to romanize several different ancient scripts to roman letter equivalents and back.

Supported scripts are:

 - greek (grc)
 - aramaic (arm)
 - syriaic (syc)
 - arabic (ara)
 - phoenician (phn)
 - brahmi (brh)
 - coptic (cop)
 - hebrew (heb)

## install

`pip install romanize3`

## Usage

Transliterate syriaic script back and forth:

```python
    import romanize3

    r = romanize3.__dict__['syc']
    print(r.convert("ܠܕܝܠܗ ܐܬܐ ܘܕܝܠܗ ܠܐ ܩܒܠܘܗܝ")) # output: LDILE ATA WDILE LA QBLWEI
    print(r.convert("LDILE ATA WDILE LA QBLWEI")) # output: ܠܕܝܠܗ ܐܬܐ ܘܕܝܠܗ ܠܐ ܩܒܠܘܗܝ
```

Filter phoenician alphabet from the given text:

```python
    r = romanize3.__dict__['phn']
    s = """𐤀𐤍𐤊 𐤕𐤁𐤍𐤕 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤁𐤍
    I, Tabnit, priest of Astarte, king of Sidon, the son
    𐤀𐤔𐤌𐤍𐤏𐤆𐤓 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆
    of Eshmunazar, priest of Astarte, king of Sidon, am lying in this sarcophagus."""
    print(r.filter(s))
```

Output:

```text
    𐤀𐤍𐤊 𐤕𐤁𐤍𐤕 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤁𐤍

    𐤀𐤔𐤌𐤍𐤏𐤆𐤓 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆

```
