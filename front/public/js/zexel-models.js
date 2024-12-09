class BaseModel {
    constructor(data = {}) {
        this.id = data.id || null;
    }
}

class PaymentModel extends BaseModel {
    constructor(data = {}) {
        super(data);
        this.source_amount = data.source_amount || 0;
        this.source_currency = data.source_currency || '';
        this.source_country = data.source_country || '';
        this.target_amount = data.target_amount || 0;
        this.target_currency = data.target_currency || '';
        this.target_country = data.target_country || '';
        this.created = data.created ? this.formatDate(data.created) : null;
        this.updated = data.updated ? this.formatDate(data.updated) : null;
        this.status = data.status || 'Draft';
        this.concept = data.concept || '';
        this.rate_exchange = data.rate_exchange || 0;
        this.sender_full_name = data.sender_full_name || '';
        this.receiver_full_name = data.receiver_full_name || '';
    }

    formatDate(date) {
        const d = new Date(date);
        const day = String(d.getDate()).padStart(2, '0');
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const year = String(d.getFullYear()).slice(-2);
        const hours = String(d.getHours()).padStart(2, '0');
        const minutes = String(d.getMinutes()).padStart(2, '0');
        return `${day}-${month}-${year} ${hours}:${minutes}`;
    }

    static STATUS_CHOICES = [
        'Draft',
        'Requested',
        'Approved',
        'Paid',
        'Deleted'
    ];
}

class CountryModel {
    constructor(data = {}) {
        this.name = data.name || '';
        this.iso3 = data.iso3 || '';
    }
}

class CurrencyModel {
    constructor(data = {}) {
        this.name = data.name || '';
        this.iso3 = data.iso3 || '';
    }
}
