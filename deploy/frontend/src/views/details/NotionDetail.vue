<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'

    import { useRouter } from 'vue-router'

    import { storeToRefs } from 'pinia'
    import { useNotionStore } from '../../store/notions'

    import NotionProjects from '../../components/notion/NotionProjects.vue'

    import Cross from '../../components/utils/Cross.vue'
    
    const { notions, notion, loading, error } = storeToRefs(useNotionStore())

    const { fetchNotions, setNotion } = useNotionStore()

    onMounted(() => {
        fetchNotions()
        setNotion()
    })

    const router = useRouter()

    const val = ref('')

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(notions, letter) {
        const filterNotion = notions.filter((item) => {
            return item.title.charAt(0).toLowerCase() === letter
        })
        return filterNotion
    }

    function filterAlphabet() {
        console.log(val.value)
        return notions.filter((items) => {
            return item.title.charAt(0).toLowerCase() === val.value
        })
    }

</script>

<template>

    <main>
        
        <div class="loading" v-if="loading">Loading notion</div>
        
        <div class="error" v-if="error">{{ error.message }}</div>
        
        <div class="notion--container">
            <div class="notion--left">
                <div 
                    v-for="(letter, index) in alphabet"
                    :key="index"
                >
                    <div 
                        v-if="filterByLetter(notions, letter).length"
                        class="lettrine">
                        {{ letter }}.
                    </div>

                    <div 
                        v-if="filterByLetter(notions, letter)" 
                        class="notion--list"
                    >
                        
                        <div 
                            
                            v-for="notion in filterByLetter(notions, letter)"
                            :key="notion.id"
                            class="notion--item"
                        >
                            <h2><router-link
                                @click="setNotion(notion)" 
                                :to="`${notion.slug}`">{{ notion.title }}</router-link></h2>

                        </div>

                    </div>

                </div>             
            </div>
            <div 
                class="notion--right"
            >
                
                <cross 
                    @click="router.push({ name: 'notions'})"
                    width="50" 
                    height="50"
                ></cross>

                <notion-projects></notion-projects>


            </div>
        </div>

    </main>

</template>

<style scoped>

.notion--list {
    flex-direction: column;
}

.notion--item {
    width: 100%;
}

</style>