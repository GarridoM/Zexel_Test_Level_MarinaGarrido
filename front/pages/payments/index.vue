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

    <div v-if="payments.length">
      <h2>{{ $t('payments_list') }}:</h2>
      <div class="table-responsive">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>{{ $t('created') }}</th>
              <th>{{ $t('concept') }}</th>
              <th>{{ $t('source_amount') }}</th>
              <th>{{ $t('source_currency') }}</th>
              <th>{{ $t('target_amount') }}</th>
              <th>{{ $t('target_currency') }}</th>
              <th>{{ $t('status') }}</th>
              <th>{{ $t('actions') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="payment in payments" :key="payment.id">
              <td>{{ payment.created }}</td>
              <td>{{ payment.concept }}</td>
              <td>{{ payment.source_amount }}</td>
              <td>{{ payment.source_currency }}</td>
              <td>{{ payment.target_amount }}</td>
              <td>{{ payment.target_currency }}</td>
              <td>{{ payment.status }}</td>
              <td>
                <button @click="handleRemovePayment(payment.id)" class="btn btn-danger btn-sm">
                  {{ $t('remove') }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="alert alert-info">
      {{ $t('no_payments') }}
    </div>

    <Alert ref="alert" />

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getPayments, removePayment } from '@/utils/client_api_zexel'
import { useI18n } from 'vue-i18n'

const payments = ref([])
const alert = ref(null)
const { t } = useI18n()

onMounted(async () => {
  try {
    payments.value = await getPayments()
  } catch (e) {
    alert.value.error(e.message)
  }
})

const handleRemovePayment = async (id) => {
  try {
    const success = await removePayment(id)
    if (success) {
      alert.value.message(t('payment_removed_successfully'))
    } else {
      alert.value.error(t('failed_to_remove_payment'))
    }
  } catch (e) {
    alert.value.error(e.message)
  }
}
</script>