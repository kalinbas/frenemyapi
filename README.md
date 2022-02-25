# frenemyapi
Simple API for frenemy Kernel Block 5 project

https://frenemyeth.herokuapp.com/api

## API methods

### **GET** /battle

### Parameters:

**p1** address or eth domain name

**p2** address or eth domain name

**steps** number of steps to generate (optional - default: 3) - must be odd number

**seed** number used for random step order (optional)

### Example call:
```
GET /battle?p1=test.eth&p2=0x7132f4b7f9E6C6721E1BcaD02f06D96c410f771a&steps=3
```

### Example output:
```
{
	"success": true,
	"p1": "test.eth",
	"p2": "0x7132f4b7f9E6C6721E1BcaD02f06D96c410f771a",
    "winner1": true,
	"steps": [
		{
			"winner1": true,
			"topic": "NFT Gains",
            "summary": "P1 hurts P2 with fireball"
			"text1": "P1 made 1.56 ETH on Opensea",
			"text2":"P2 lost 4.5 ETH flipping JPEGs"
        },
        {
			"winner1": false,
			"topic": "Rugpull Participation",
			"summary": "P2 hurts P1 with mega-punch"
			"text1": "P1 lost 100 ETH to 3 rugpulls",
			"text2":"P2 never lost to anything we know about"

        },
        {
			"winner1": true,
			"topic": "NFT Count",
			"summary": "P1 hurts P2 with super-flash"
			"text1": "P1 is a pro with 100 NFTs",
			"text2":"P2 is a noob with 2 NFTs"

        }
	]
}
```

### Example error:
```
{
	"success": false,
	"error": "Data couldn’t be loaded"
}
```


## Run server locally
```
pip install -r requirements.txt 
gunicorn server:app
```