import axios from 'axios'

class Resource {
  constructor (http, root) {
    this.list = () => http.get(`/${root}s`)
    this.create = (data) => http.put(`/${root}s`, { data: data })
    this.get = (id) => http.get(`/${root}/${id}`)
    this.update = (id, diff) => http.put(`/${root}/${id}`, { data: diff })
    this.delete = (id) => http.delete(`/${root}/{id}`)
  }
}

class API {
  constructor (env) {
    let baseURL = `${env.VUE_APP_BACKEND_DOMAIN}/api/v${env.VUE_APP_API_VERSION}`
    let http = axios.create({
      baseURL: baseURL
    })
    this.http = http

    // Resources
    this.post = new Resource(http, 'post')
    this.circle = new Resource(http, 'circle')
  }
}

export default new API(process.env)
