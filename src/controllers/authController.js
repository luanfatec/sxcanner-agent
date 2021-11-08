const fs = require("fs");
const messages = require("../helper/messages");

/**
 * ...
 */

module.exports = class AuthController {
    checkLoginKey(request, response, next) {
        const { token } = request.body;

        fs.readFile(`${__dirname}/../.db/auth.json`, 'utf-8', (err, jsonFile) => {
            let db = JSON.parse(jsonFile); // Load json parse...
            let active = false;

            // Checa se a chave existe dentro do .db json...
            for(let data in db) {
                if (db[data].loginKey === token) {        
                    active = true; // Caso exista, estará ativando a flag active...
                    break;
                }                
            }


            // Caso a flag não seja ativada pela chave, será retornado uma mensagem de não autorizado ao request...
            if (!active) {
                return response.status(403).json({
                    "message": messages.cpuController.errorPageForbidden
                });
            }

            next();
        });  
               
    }
}
