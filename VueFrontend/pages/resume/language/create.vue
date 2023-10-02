<template>
    <div class="row py-3">
        <div class="col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Language Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New Language
                                <NuxtLink :to="'/resume/language'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-list-ol"></i>{{ ' ' }}List
                                </NuxtLink>
                            </p>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <form @submit.prevent="CreatenewLanguage" class="form form-horizontal needs-validation"
                                    novalidate>
                                    <div class="form-body">
                                        <div class="row">

                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="card_title">Card
                                                        Title</label>
                                                    <div class="col-md-9">
                                                        <select v-model="newLanguage.card_title"
                                                            class="form-select border-primary"
                                                            aria-label="Default select example" required>
                                                            <option disabled value="">Please Select</option>
                                                            <option>Language</option>
                                                            <option>Spoken Language</option>
                                                        </select>
                                                        <span class="invalid-feedback">Please Select Card
                                                            Title</span>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="language_name">Language
                                                        Name</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newLanguage.language_name" type="text"
                                                            id="language_name" class="form-control border-primary"
                                                            placeholder="Language Name" name="language_name" required>
                                                        <span class="invalid-feedback">Language Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>

                                        </div>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control"
                                                        for="profeciency_level">Proficiency Level</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newLanguage.profeciency_level" type="text"
                                                            id="profeciency_level" class="form-control border-primary"
                                                            placeholder="Proficiency Level" name="profeciency_level"
                                                            required>
                                                        <span class="invalid-feedback">Proficiency Level is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>

                                        </div>

                                    </div>

                                    <div class="row">
                                        <div class="form-actions my-2">
                                            <NuxtLink :to="'/resume/language'"
                                                class="btn btn-sm btn-danger mx-2 float-start">
                                                <i class="bi bi-x-lg"></i>{{ ' ' }}Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-sm btn-primary mx-2 float-end">
                                                <i class="bi bi-check2-square"></i>{{ ' ' }}Save
                                            </button>

                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'CreateLanguage',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const newLanguage = ref({});
        const router = useRouter();

        const CreatenewLanguage = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/language/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newLanguage.value),
                })
                    .then(function (response) {
                        router.push('/resume/language');
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            } else {
                form.classList.add('was-validated');
            };
        };

        onMounted(() => {
            const forms = document.querySelectorAll('.needs-validation');

            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    event.preventDefault();
                    event.stopPropagation();

                    if (!form.checkValidity()) {
                        form.classList.add('was-validated');
                    } else {
                        CreatenewLanguage();
                    }
                }, false);
            });
        });

        return {
            newLanguage,
        };
    },
});
</script>
  
<style></style>
  