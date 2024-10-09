export const base_api_url = "http://localhost:8080";

class Queue {
    static async getAll(){
    }
}

export async function getToken(){
    const username = "admin";
    const password = "admin12345";

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);
    
    const response = await fetch(`${base_api_url}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
    });
    if (response.ok) {
        const data = await response.json();
        console.log(data.access_token);
    } else {
        console.log("Ошибка входа.")
    }

    
}
