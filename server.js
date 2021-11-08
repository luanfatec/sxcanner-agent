const app = require("./.init/express-app");
const axios = require('axios');
const argv = require('minimist')(process.argv.slice(2));


app.listen(3333, () => {
    const date = new Date();
    console.log(`XScanner Agent started: [${date.toString()}]`);
});

if (argv.typescan === "runningagent") {
    setInterval(() => {

        // ...
        axios({
            url: 'http://localhost:3333/single-ports-check',
            method: "POST",
            data: {
                token: "YXBwLXphYmJpeC1zZXJ2ZXItbG9naW4K"
            },
            headers: {
                contentType: "application/json"
            }
        }).then(function (response) {
            console.log(response.data);

        }).catch(function (error) {
            console.log(error);

        });

        // ...
        axios({
            url: 'http://localhost:3333/check-history-port',
            method: "POST",
            data: {
                token: "YXBwLXphYmJpeC1zZXJ2ZXItbG9naW4K"
            },
            headers: {
                contentType: "application/json"
            }
        }).then(function (response) {
            console.log(response.data);

        }).catch(function (error) {
            console.log(error);

        });

        // ...
        axios({
            url: 'http://localhost:3333/check-history-por-advanced',
            method: "POST",
            data: {
                token: "YXBwLXphYmJpeC1zZXJ2ZXItbG9naW4K"
            },
            headers: {
                contentType: "application/json"
            }
        }).then(function (response) {
            console.log(response.data);

        }).catch(function (error) {
            console.log(error);

        });

    }, 3000);

}