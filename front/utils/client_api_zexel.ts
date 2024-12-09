export async function getPayments() {
    const response = await fetch('http://localhost:8000/api/payments/', {
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    const data = await response.json()
    return data.map(item => new PaymentModel(item))
}

export async function removePayment(id: number): Promise<boolean> {
    try {
        const response = await fetch(`http://localhost:8000/api/payments/${id}/`, {
            method: 'DELETE'
        });
        return response.ok;
    } catch (error) {
        console.error('Error removing payment:', error);
        return false;
    }
}
