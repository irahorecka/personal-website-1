clean:
	rm -rf ./personalWebsite/__pycache__

production:
	sed -i extension 's/localhost:5000/irahorecka/g' ./personalWebsite/static/script.js
	rm ./personalWebsite/static/script.jsextension

local:
	sed -i extension 's/irahorecka/localhost:5000/g' ./personalWebsite/static/script.js
	rm ./personalWebsite/static/script.jsextension
