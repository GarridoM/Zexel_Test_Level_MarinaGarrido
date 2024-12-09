export async function getCountries() {
    const response = await fetch('https://countriesnow.space/api/v0.1/countries/states', {
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    const data = await response.json()
    return data['data'].map(item => new CountryModel(item))
}
