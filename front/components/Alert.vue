<template>
    <div v-if="showModal" class="alert alert-danger" role="alert">
        {{ alertMessage }}
        <button type="button" class="close" @click="hide" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</template>

<script setup>
const showModal = ref(false);
const alertMessage = ref("");
const typeAlert = ref('');

const show = () => {
    showModal.value = true;
};

const hide = () => {
    showModal.value = false;
};

const message = (message, showModal = true) => {
    typeAlert.value = 'message';
    __write(message, showModal);
};

const error = (message, showModal = true) => {
    typeAlert.value = 'error';
    __write(message, showModal);
};

const __write = (message, showModal = true) => {
    alertMessage.value = "";
    alertMessage.value = message;
    if (showModal) {
        show();
    }
};

defineExpose({
    show, hide, message, error
})
</script>