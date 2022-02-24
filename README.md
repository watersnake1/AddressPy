# Python ETH Wallet Generator
Generates wallets to be used with chains such as ETH, Avax, FTM, etc. Requires a few dependencies from pip in order to function, which can be installed using the accompanying script. The output of the script is a csv file with private keys and addresses. It is advisable to NOT store your keys long term in this format, but rather to either 1) put them directly into geth, a hardware wallet or something else, then nuke the keys, or 2) immediately create keystores of them andstore the pk behind a password.

## How make keystore?
Pretty simple, actually. I don't think web3.py let's you do this without connecting to geth, but there is a quick and dirty method I found on the internet. Use `npm install ethereumjs-wallet`, then in a node console run:

```
node
>const Wallet = require('ethereumjs-wallet').default;
>var key = Bytes.from('{privatekey}', 'hex');
>var wallet = Wallet.fromPrivateKey(key);
>var keystore = wallet.toV3String('<password>');
```
This gives you a promise that will eventually return a keystore. NOTE: While testing this I happened to notice that Metamask is really slow to decrypt these and import them for some reason. In order to import to metamask, first you save the output (without the outer single quotes) in a .json file then open metamask and click 'import account' -> 'from file' and select the file and enter the password you used above.

## Usage of this script
`python3 generate.py`

