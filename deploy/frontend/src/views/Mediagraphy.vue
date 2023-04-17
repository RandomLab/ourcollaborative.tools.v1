<script setup>

     import { ref, reactive, computed, onMounted } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useReferenceStore } from '../store/references'

    import { formatDate } from '../mixins/formatDateMixin'
    import { cleanURL } from '../mixins/cleanURL'

    const { references, loading, error } = storeToRefs(useReferenceStore())

    const { fetchReferences } = useReferenceStore()

    onMounted(() => {
        fetchReferences()
    })

    const mediaTypes = ['book', 'article', 'thesis', 'videos', 'websites', 'video games', 'podcasts']

    function filterByType(references, type) {
        const filterReferences = references.filter((item) => {
            return item.media_type === type
        })
        return filterReferences
    }

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{ error.message }}</div>

        <div class="reference--container">
             <div 
                v-for="(type, index) in mediaTypes"
                :key="index"
                class="reference--index"
            >
                <div 
                    v-if="filterByType(references, type).length"
                    class="lettrine">
                    {{ type }}
                </div>

                <div
                    v-if="filterByType(references, type)"
                    class="reference--list"
                >  

                    <div
                        v-for="reference in filterByType(references, type)"
                        :key="reference.id"
                        class="reference--item"
                    >
                        <h1>{{ reference.title }}</h1>
                        <h1 v-if="reference.subtitle">{{ reference.subtitle }}</h1>
                        <h2>{{ reference.author }}</h2>
                        <h2 v-if="reference.editor">{{ reference.editor }}</h2>
                        <p>{{ formatDate(reference.date_pub) }}</p>
                        <p v-if="reference.pages ">{{ reference.pages }}</p>
                        <p v-if="reference.url"><a :href="reference.url">{{ cleanURL(reference.url) }}</a></p>

                    </div>
                </div>               
            </div>
        </div>
    </main>

</template>