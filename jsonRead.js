const bResp = require('./input.json');

const randInt = function(min, max) {
	return Math.floor(Math.random() * (max - min) ) + min;
};

const strProcess = function(str) {
	let noLowers; /* will contain string with no capitals */
	let noSymbols; /* string stripped of symbols */

	noLowers = str.toLowerCase();
	noSymbols = noLowers.replace(/[^a-zA-Z ]/g, "");

	return noSymbols;
};

const keywordDecider = function(str) {
	let word; /* contains word from a given string */
	let eStatus; /* determines when to stop the function */
};

/*	Kanade Bot Message Handler ( but in Javascript ) */
const responder = function(keyword) { /* prototyping the main message handler */
	let respStep; /* variable that counts out responses */
	let ran; /* variable that is use to determines whether to send a response or not */
	let respRan; /* variable that decides what response to send*/

	for (objStep = 0; objStep != bResp.length;) { /* Goes through each json object in bResp array */
		respStep = 0;

		if (keyword == bResp[objStep].keywords[0]) {
			switch(bResp[objStep].type) {
				case 0: /* standard text response */
//					ran = randInt(bResp[objStep].rarity[0], bResp[objStep].rarity[1]); /* Takes rarity from the selected object */
					ran = 1;
					if (ran == 1) {
						return bResp[objStep].responses[randInt(0, bResp[objStep].responses.length)];
					}
					return
				case 1: /* multi-message text response */
//					ran = randInt(bResp[objStep].rarity[0], bResp[objStep].rarity[1]); /* Takes rarity from the selected object */
					ran = 1;
					if (ran == 1) {
						while (respStep < bResp[objStep].responses.length) {
							console.log(bResp[objStep].responses[respStep]);
							console.log('⠀');
							respStep++;
						}
					return;
					}
				case 2: /* image response */
//					ran = randInt(bResp[objStep].rarity[0], bResp[objStep].rarity[1]); /* Takes rarity from the selected object */
					ran = 1;
					if (ran == 1) {
						return bResp[objStep].responses[randInt(0, bResp[objStep].responses.length)];
					}
					return;
			}
		} else objStep++;
	}
};

console.log(strProcess('I #$@$#LOVE $%#%#$%$#GRACE'));
//responder('grace');
if ('5' in '23451') console.log("haha");
