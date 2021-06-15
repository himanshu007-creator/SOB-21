# Summer-of-BitCoin'21

## Coding task

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

> **_Contents_**

- Solution Approach
- ✨References ✨

## Solution Approach

My code first Parses the CSV file and stores it a list.
Each entry (Transaction) in list is given a class Transaction that helps to get various data from each transaction. Then each transaction thus available is checked to be a valid transaction, i,e checked that it have a parent and the total weight of block still stays under 400000. If conditions are met, Transaction is validated and stored in Transaction block.

Then for each Transaction in Transaction_block, its txid is stored in block_sample.txt with each entry separated by a newline.

## References

| Name                          | Link                                                               |
| ----------------------------- | ------------------------------------------------------------------ |
| Python Documentation          | https://docs.python.org/3/                                         |
| Bitcoin Transaction Explained | https://www.bitcoin.com/get-started/how-bitcoin-transactions-work/ |

### P.S

Sorry for the delay :-)
