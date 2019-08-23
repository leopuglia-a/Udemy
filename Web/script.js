var database = [
	{
		username: "andrei",
		password: "supersecret"
	}
	{
		username: "ingrid",
		password: "123"
	}
	{
		username: "sally",
		password: "1"
	}
];

var newsfeed = [
	{
		username: "Bobby",
		timeline: "So tired from all that learning!"
	},
	{
		username: "Sally",
		timeline: "Javascript is sooooo cool!"
	},
	{
		username: "Mitch",
		timeline: "Javascript is preeetyy cool!"
	}
];

var userNamePrompt = prompt("username");
var passwordPrompt = prompt("password");

function validUser(username, password) {
	for (var i = 0; i < database.length; i++) {
		if (user === database[i].username && password === database[i].password) {
			return true;
		}
	return false
}

function signIn(user, password) {
	for (var i = 0; i < database.length; i++) {
		if (validUser(user, password)) {
			alert("Successfully logged in");
			console.log(newsfeed);
		} else {
			alert("Incorrect username or password");
		}
		
	}

}

signIn(userNamePrompt,passwordPrompt);