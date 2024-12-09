<template>
  <div class="container mt-5 pt-4">

    <h1 class="display-4 mt-2 mb-4">{{ $t('countries') }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t('app_description') }}</h2>
      <div class="divider"></div>
    </div>

    <div>
      <h2 class="h4 mb-3">{{ $t('main_functions') }}</h2>
      <div class="d-flex justify-content-between">
        <NuxtLink to="/countries" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('list_countries') }}</div>
        </NuxtLink>
        <NuxtLink to="/countries/search" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('search_countries') }}</div>
        </NuxtLink>
        <NuxtLink to="/countries/detail" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('detail_countries') }}</div>
        </NuxtLink>
        <NuxtLink to="/countries/edit" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('edit_countries') }}</div>
        </NuxtLink>
      </div>
    </div>

    <div v-if="countries.length">
      <h2>{{ $t('countries_list') }}:</h2>
      <div class="table-responsive">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>{{ $t('name') }}</th>
              <th>{{ $t('iso3') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="country in countries" :key="country.iso3">
              <td>{{ country.name }}</td>
              <td>{{ country.iso3 }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="alert alert-info">
      {{ $t('no_countries') }}
    </div>

    <Alert ref="alert" />

  </div>
</template>

<script setup>
const countries = ref([])
const alert = ref(null)

onMounted(async () => {
  try {
    countries.value = await getCountries()
  } catch (e) {
    alert.value.error(e.message)
  }
})
</script>