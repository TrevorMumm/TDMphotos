# TDM_Photography#

Needs media folder stored on google cloud storage

pushing to heroku:
git push heroku main

login to heroku
heroku login

Photoshop Infrared Workflow
Adjust white balance for Infrared
	Temp: 2200
	Adjust tint to stay cool without too much green or yellow, usually -#
	
Open in Photoshop
	Add adjustment layer -> Color Mixer
		Red channel:
			Red 0%
			Green 0%
			Blue 100%
		Blue channel:
			Red: 100%
			Green: 0%
			Blue: 0%
		Green:
			Red: 0%
			Green: 70%-100%
			Blue: 0%
	Add adjustment layer -> Saturation/Hue
		Adjust Hue towards the right (Magenta) until desired color acheived
		Adjust saturation for desired affect