import axios from 'axios';

const API_URL = 'http://christgg1997.pythonanywhere.com/api_v1.0';


/* -------------------------------------------------------------------------- */
/*                                    USER                                    */
/* -------------------------------------------------------------------------- */

export async function getUser() {
  try {
    const response = await axios.get(API_URL + '/user');
    const userData = response.data;
    return userData;
  } catch (error) {
    console.error(error);
  }
}

async function postUser(data: any) {
    const url = `${API_URL}/user`;
    try {
        const response = await axios.post(url, data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}


async function postLogin(data: any) {
    try {
        const response = await axios.post(API_URL + '/login', data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}

export async function putUser(id: string, data: any) {
    const url = `${API_URL}/user/${id}`;
    try {
        await axios.put(url, data);
        console.log("response", "Success");
    } catch (error) {
        console.error(error);
    }
}


/* -------------------------------------------------------------------------- */
/*                                  PAQUETES                                  */
/* -------------------------------------------------------------------------- */

async function getPackage() {
    try {
        const response = await axios.get(API_URL + '/package');
        const paquetesData = response.data;
        return paquetesData;
    } catch (error) {
        console.error(error);
    }
}

async function getPackageById(id: string) {
    const url = `${API_URL}/package/${id}`;
    try {
        const response = await axios.get(url);
        const packageData = response.data;
        return packageData;
    } catch (error) {
        console.error(error);
    }
}

async function updatePackage(id: string, data: any) {
    const url = `${API_URL}/package/${id}`;
    try {
        const response = await axios.put(url, data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}

/* -------------------------------------------------------------------------- */
/*                                 PRODUCTION                                 */
/* -------------------------------------------------------------------------- */

async function getProduction(id: string) {
    try {
        const url = `${API_URL}/production/${id}`;
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}


async function getProductionId(id: string) {
    const url = `${API_URL}/production/${id}`;
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}

async function postProduction(data: any) {
    const url = `${API_URL}/production`;
    try {
        const response = await axios.post(url, data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}

async function putProduction(id: string, data: any) {
    const url = `${API_URL}/production/${id}`;
    try {
        await axios.put(url, data);
        console.log("response", "Success");
    } catch (error) {
        console.error(error);
    }
}

/* -------------------------------------------------------------------------- */
/*                                   PRODUCT                                  */
/* -------------------------------------------------------------------------- */

async function getProduct() {
    const url = `${API_URL}/product`;
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}

async function postProduct(data: any) {
    const url = `${API_URL}/product`;
    try {
        const response = await axios.post(url, data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}

async function putProduct(id: string, data: any) {
    const url = `${API_URL}/product/${id}`;
    try {
        await axios.put(url, data);
        console.log("response", "Success");
    } catch (error) {
        console.error(error);
    }
}

async function getProductById(id: string) {
    const url = `${API_URL}/product/${id}`;
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}

/* -------------------------------------------------------------------------- */
/*                                    LABES                                   */
/* -------------------------------------------------------------------------- */

async function getLabel() {
    const url = `${API_URL}/label`;
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}

async function postLabel(data: any) {
    const url = `${API_URL}/label`;
    try {
        const response = await axios.post(url, data);
        const responseData = response.data;
        return responseData;
    } catch (error) {
        console.error(error);
    }
}

async function putLabel(id: string, data: any) {
    const url = `${API_URL}/label/${id}`;
    try {
        await axios.put(url, data);
        console.log("response", "Success");
    } catch (error) {
        console.error(error);
    }
}

async function getLabelById(id: string) {
    const url = `${API_URL}/label/${id}`;
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}
















