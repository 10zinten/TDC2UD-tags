# TDC2UD-tags
Adaptation of TDC ([Tibetan In Digital Communication](http://larkpie.net/tibetancorpus/#pos)) data by turning POS tags to [UD POS tags](http://universaldependencies.org/u/pos/) in order to train [RDRPOSTagger](https://github.com/datquocnguyen/RDRPOSTagger)

## Usage
```
$ python formatter.py --input_data data/mdzangs_blun-niceline-UD.txt
```
`goldTrain` file (TDC dataset in RDRPOSTagger format) will the generated at `data/`.
