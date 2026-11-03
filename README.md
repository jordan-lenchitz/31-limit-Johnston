# 31-limit-johnston

- 31-limit calculator for note names
- in extended just intonation
- using ben johnstons system
- turns a ratio x/y or x y into a 31-limit johnston note name
- returns the prime factor larger than 31 otherwise

## usage
```bash
cargo run -- 49/55
# output Cb77v+

cargo run -- 3 2
# output G

cargo run -- 23/16
# output F#23+
```

## johnston notation symbols

outputs consist of a letter name plus some combination of `#b7L^v3e+-` and the higher-limit prime symbols `17`, `19`, `23`, `29`, `31` (and `v17`, `v19`, `v23`, `v29`, `v31`)

- `# b + -` and `7` correspond directly to their johnston notation symbols
- `L` = upside down 7
- `^` = up arrow
- `v` = down arrow
- `3` = 13
- `e` = upside down 13
- `17`, `19`, `23`, `29`, `31` = 17-, 19-, 23-, 29-, and 31-limit accidentals
- `v17`, `v19`, `v23`, `v29`, `v31` = upside down 17, 19, 23, 29, and 31

## references

john fonville's article from 1991:
### - [`ben johnston's extended just intonation: a guide for interpreters`](https://www.jstor.org/stable/833435)

timothy ernest johnson's dissertation from 2008:
### - [`13-limit extended just intonation in ben johnston’s string quartet no. 7 and toby twining’s chrysalid requiem, ‘gradual/tract’`](https://www.proquest.com/openview/f9d0a27d5b2d659c700412aa241f7265/)
