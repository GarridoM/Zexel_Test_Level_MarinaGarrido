<template>
  <div class="container mt-5 pt-4">

    <h1 class="display-4 mt-2 mb-4">{{ $t('payments') }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t('app_description') }}</h2>
      <div class="divider"></div>
    </div>

    <div>
      <h2 class="h4 mb-3">{{ $t('main_functions') }}</h2>
      <div class="d-flex justify-content-between">
        <NuxtLink to="/payments" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('list_payments') }}</div>
        </NuxtLink>
        <NuxtLink to="/payments/add" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('add_payments') }}</div>
        </NuxtLink>
        <NuxtLink to="/payments/edit" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('edit_payments') }}</div>
        </NuxtLink>
      </div>
    </div>

    <div>
      <h2>{{ $t('add_payments') }}</h2>
      <form @submit.prevent="submitPayment">
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="sourceAmount" class="form-label">{{ $t('source_amount') }}</label>
            <input type="number" class="form-control" id="sourceAmount" v-model="payment.source_amount" required>
          </div>
          <div class="col-md-4">
            <label for="sourceCurrency" class="form-label">{{ $t('source_currency') }}</label>
            <input type="text" class="form-control" id="sourceCurrency" v-model="payment.source_currency" required>
          </div>
          <div class="col-md-4">
            <label for="sourceCountry" class="form-label">{{ $t('source_country') }}</label>
            <input type="text" class="form-control" id="sourceCountry" v-model="payment.source_country" required>
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="targetAmount" class="form-label">{{ $t('target_amount') }}</label>
            <input type="number" class="form-control" id="targetAmount" v-model="payment.target_amount" required>
          </div>
          <div class="col-md-4">
            <label for="targetCurrency" class="form-label">{{ $t('target_currency') }}</label>
            <input type="text" class="form-control" id="targetCurrency" v-model="payment.target_currency" required>
          </div>
          <div class="col-md-4">
            <label for="targetCountry" class="form-label">{{ $t('target_country') }}</label>
            <input type="text" class="form-control" id="targetCountry" v-model="payment.target_country" required>
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="concept" class="form-label">{{ $t('concept') }}</label>
            <input type="text" class="form-control" id="concept" v-model="payment.concept" required>
          </div>
          <div class="col-md-4">
            <label for="senderFullName" class="form-label">{{ $t('sender_full_name') }}</label>
            <input type="text" class="form-control" id="senderFullName" v-model="payment.sender_full_name" required>
          </div>
          <div class="col-md-4">
            <label for="receiverFullName" class="form-label">{{ $t('receiver_full_name') }}</label>
            <input type="text" class="form-control" id="receiverFullName" v-model="payment.receiver_full_name" required>
          </div>
        </div>
        <button type="submit" class="btn btn-primary">{{ $t('submit') }}</button>
      </form>
    </div>

    <Alert ref="alert" />

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const { t } = useI18n()

const payment = ref({
  source_amount: null,
  source_currency: '',
  source_country: '',
  target_amount: null,
  target_currency: '',
  target_country: '',
  concept: '',
  sender_full_name: '',
  receiver_full_name: ''
})
const alert = ref(null)

const submitPayment = async () => {
  try {
    // Make an API call to submit the payment
    const response = await fetch('http://localhost:8000/api/payments/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payment.value),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    console.log('Payment added:', result);

    alert.value.message(t('payment_added_successfully'))

    // Reset the form after successful submission
    payment.value = {
      source_amount: null,
      source_currency: '',
      source_country: '',
      target_amount: null,
      target_currency: '',
      target_country: '',
      concept: '',
      sender_full_name: '',
      receiver_full_name: ''
    }
  } catch (error) {
    alert.value.error(t('error_adding_payment', { error: error.message }))
  }
}
</script>