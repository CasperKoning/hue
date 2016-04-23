### What is this?
This is a repository in which I store information on controlling my Phillips Hue lights

### Getting started:
1) Connect Hue to router
2) Press link button to connect it to your Hue lights
3) Get IP address for Hue Bridge, easy way: www.meethue.com/api/nupnp
2) Press the link button again and `POST` on `http://<bridge_ip>/api` with body:
```
{
"devicetype":"your_device_type"
}
```
This will respond with an authorized username:
```
[
	{
		"success": {
			"username": "some_username"
		}
	}
]
```
3) `GET` on `/api/<username>` will respond with all information on the linked Bridge.
4) `GET` on `api/<username>/lights` will respond with only the information on the connected lights.
5) `GET` on `api/<username>/ligths/<index>` will respond with only the information on the ligth with the relevant index.
6) Updating the state of a light can be done by `PUT`ing on `http://<bridge_ip>/api/<username>/lights/<index>/state`,
 e.g. to turn a light off just `PUT` with the body
```
{
"on":false
}
```
The schema of state is as follows:
```
"state": {
		"on": <boolean>,
		"bri": <int: 0 .. 254>,
		"hue": <int 0 .. 65535>,
		"sat": <int 0 .. 254>,
		"effect": "none",
		"xy": [
			<double>,
			<double>
		],
		"ct": <int>,
		"alert": "none",
		"colormode": <colormode_enum>/<string>,
		"reachable": <boolean>
}
```

More on the Hue API can be found [here](http://www.developers.meethue.com/documentation/core-concepts)