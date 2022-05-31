/* main.js
 *
 * Kanade Bot in JavaScript
 * Nanahira Monke Kanade Dev
 *
 * */

console.log("Kanade Bot");

const { Client, Intents } = require('discord.js');i /*!important/import for discord.js*/

require('dotenv').config(); /* Loads the .env file in working directory */

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS, Intents.FLAGS.GUILD_BANS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.DIRECT_MESSAGES] });

/* Runs when the bot is ready, Sets status. */
client.once('ready', () => {
	console.log('Ready');
	if (process.env.DEBUG_VALUE != 0) client.user.setActivity("KANADE BOT JS");
	else client.user.setActivity("placeholder");
});

/* Message response event handler (this will be interesting) */
client.on("messageCreate", message => {
	if (message.author.id == 840279273021636628) return; /* Ignores self. */

	message.channel.send('placeholder message');
	return;
});

/* Logs in the bot using a token from your local .env */
client.login(process.env.DISCORD_TOKEN);
