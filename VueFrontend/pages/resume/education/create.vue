<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Education</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Create New Education
                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-danger float-end"><i
                                            class="bi bi-arrow-left-circle"></i>Back
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <form class="form form-horizontal">
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="course_title">Course
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="course_title"
                                                                class="form-control border-primary"
                                                                placeholder="Course Title" name="course_title">
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="card_title">Card
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="card_title"
                                                                class="form-control border-primary" value="Education"
                                                                placeholder="Card Title" name="card_title">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="school_name">School
                                                            Name</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="school_name"
                                                                class="form-control border-primary"
                                                                placeholder="School Name" name="school_name">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Location</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="location"
                                                                class="form-control border-primary" placeholder="Location"
                                                                name="location">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="education_level">Education Level</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="education_level"
                                                                class="form-control border-primary"
                                                                placeholder="Education Level" name="education_level">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="final_grade">Final
                                                            Grade</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="final_grade"
                                                                class="form-control border-primary"
                                                                placeholder="Final Grade" name="final_grade">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="start_date">Start
                                                            Date</label>
                                                        <div class="col-md-9">
                                                            <input type="date" id="start_date"
                                                                class="form-control border-primary" placeholder="Start
                                                            Date" name="start_date">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="end_date">End
                                                            date</label>
                                                        <div class="col-md-9">
                                                            <input type="date" id="end_date"
                                                                class="form-control border-primary" placeholder="End date"
                                                                name="end_date">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="form-actions float-end mt-2">
                                            <NuxtLink :to="'/resume/education'" class="btn btn-danger mx-2">
                                                <i class="bi bi-x-lg"></i> Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-primary mx-2">
                                                <i class="bi bi-check2-square"></i> Save
                                            </button>
                                        </div>
                                    </form>
                                </div>
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
    name: 'CreateUser',
    setup() {
        
        definePageMeta({
            layout: "sidestar",
        });
        
        const axios = useNuxtApp().$axios;
        const newUser = ref({ phone_number: '', email: '', password: '' });
        const errorMessageEmail = ref('');
        const errorMessagePhone = ref('');
        const isErrorPhone = ref('form-control');
        const isErrorEmail = ref('form-control');
        const router = useRouter();

        const createUser = async () => {
            const form = document.querySelector('.needs-validation');
            errorMessageEmail.value = '';
            errorMessagePhone.value = '';
            isErrorPhone.value = 'form-control';
            isErrorEmail.value = 'form-control';
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: '/user',
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newUser.value),
                })
                    .then(function (response) {
                        console.log('Registration successful');
                        errorMessageEmail.value = '';
                        errorMessagePhone.value = '';
                        isErrorPhone.value = 'form-control';
                        isErrorEmail.value = 'form-control';
                        router.push('/auth/login');
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                        if (error.response.data.detail['Email Exists']) {
                            errorMessageEmail.value = 'Email Already Exists';
                            isErrorPhone.value = 'form-control';
                            isErrorEmail.value = 'form-control border-danger';
                        } else if (error.response.data.detail['Phone Number Exists']) {
                            errorMessagePhone.value = 'Phone Number Already Exists';
                            isErrorPhone.value = 'form-control border-danger';
                            isErrorEmail.value = 'form-control';
                        }
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
                        errorMessageEmail.value = '';
                        errorMessagePhone.value = '';
                        isErrorPhone.value = 'form-control';
                        isErrorEmail.value = 'form-control';
                    } else {
                        createUser();
                    }
                }, false);
            });
        });

        if (errorMessagePhone || errorMessageEmail) {
            return {
                newUser,
                errorMessagePhone,
                errorMessageEmail,
                isErrorEmail,
                isErrorPhone
            }
        } else {
            return {
                newUser,
                createUser,
            };
        }

    },
});
</script>
  
<style></style>
  