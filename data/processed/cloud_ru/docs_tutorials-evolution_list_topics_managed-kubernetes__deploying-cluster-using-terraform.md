---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__deploying-cluster-using-terraform.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 72.74
tokens: 9437
characters: 7179
timestamp: 2025-12-24T05:53:02.012798
finish_reason: stop
---

### Развертывание кластера Managed Kubernetes с помощью Terraform

С помощью этого руководства вы научитесь автоматически развертывать инфраструктуру в облаке Cloud.ru Evolution при помощи инструмента Terraform на примере создания кластера Managed Kubernetes.

Вы будете использовать следующие сервисы:

• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
• Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
• Terraform — инструмент для управления IaC.

Шаги:

1. Установите и настройте Terraform.
2. Настройте конфигурационный файл main.tf.
3. Создайте кластер Managed Kubernetes с помощью Terraform.
4. Проверьте создание кластера и подключитесь к нему.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте ключ доступа и сохраните Key ID (логин) и Key Secret (пароль). Это данные для аутентификации и подключения к сервисам Cloud.ru вашего проекта.
3. Создайте сервисный аккаунт для интеграции с другими сервисами облака Evolution вашего проекта.
4. Установите инструмент для работы с кодом, например Visual Studio Code, или используйте стандартный терминал, например bash, cmd или PowerShell.

1. Установите и настройте Terraform

1. Установите Terraform.
2. Установите Terraform-провайдер.
   Шаг с командой `terraform init` пока пропустите.
3. Проверьте, что установка прошла корректно:

```bash
terraform --version
```

Должна отобразиться версия Terraform.

2. Настройте конфигурационный файл main.tf

1. Создайте локальную папку для проекта.
2. В папке проекта создайте файл main.tf и добавьте в него код:

```hcl
provider "cloudru" {
  project_id = "<your-project-id>"
  auth_key_id = "<your-key-id>"
  auth_secret = "<your-key-secret>"
  iam_endpoint = "iam.api.cloud.ru:443"
  k8s_endpoint = "mk8s.api.cloud.ru:443"
}

data "cloudru_k8s_zone_flavors" "k8s_zones" {}

resource "cloudru_k8s_cluster" "kube" {
  name = "tf-cluster"
  control_plane = {
    count = 1
    type = "MASTER_TYPE_SMALL"
    version = "v1.32.5"
    zones = [data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)+1]]
  }
  network_configuration = {
    services_subnet_cidr = "10.0.0.0/20"
    nodes_subnet_cidr = "192.168.20.0/24"
    pods_subnet_cidr = "172.16.0.0/12"
    kube_api_internet = true
  }
}

resource "cloudru_k8s_nodepool" "kuber_nodepool" {
  cluster_id = cloudru_k8s_cluster.kube.id
  name = "tf-worker-pool"
  zone = data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)+1]
  scale_policy = {
    fixed_scale = {
      count = 1
    }
  }
  hardware_compute = {
    disk_size = 10
    disk_type = "DISK_TYPE_SSD_HDD"
    flavor_id = data.cloudru_k8s_zone_flavors.k8s_zones.flavors[index(data.cloudru_k8s_zone_flavors.k8s_zones.flavors..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.flavors..index)+1]
  }
  nodes_network_configuration = {
    nodes_subnet_cidr = "192.168.123.0/24"
  }
  depends_on = [
    cloudru_k8s_cluster.kube
  ]
}
```

Где:
• `<your-project-id>` — идентификатор проекта.
• `<your-key-id>` — логин ключа доступа, который вы создали перед началом работы.
• `<your-key-secret>` — пароль ключа доступа, который вы создали перед началом работы.

3. Сохраните файл main.tf. С помощью него вы задали конфигурацию для провайдера Terraform и точки обращения к сервисам Cloud.ru.
4. В терминале перейдите в папку проекта и выполните команду:

```bash
terraform init
```

Если все прошло успешно, вы увидите похожий текст:

```
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work.
If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.
```

3. Создайте кластер Managed Kubernetes с помощью Terraform

На этом шаге вы создадите файл конфигурации и примените его.

1. В каталоге проекта создайте файл конфигурации kuber.tf и добавьте в него код:

```hcl
data "cloudru_k8s_zone_flavors" "k8s_zones" {}

# Creating a k8s cluster / master nodes
resource "cloudru_k8s_cluster" "kube" {
  name = "tf-cluster"
  control_plane = {
    count = 1
    type = "MASTER_TYPE_SMALL"
    version = "v1.32.5"
    zones = [data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)+1]]
  }
  network_configuration = {
    services_subnet_cidr = "10.0.0.0/20"
    nodes_subnet_cidr = "192.168.20.0/24"
    pods_subnet_cidr = "172.16.0.0/12"
    kube_api_internet = true
  }
}

resource "cloudru_k8s_nodepool" "kuber_nodepool" {
  cluster_id = cloudru_k8s_cluster.kube.id
  name = "tf-worker-pool"
  zone = data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones..index)+1]
  scale_policy = {
    fixed_scale = {
      count = 1
    }
  }
  hardware_compute = {
    disk_size = 10
    disk_type = "DISK_TYPE_SSD_HDD"
    flavor_id = data.cloudru_k8s_zone_flavors.k8s_zones.flavors[index(data.cloudru_k8s_zone_flavors.k8s_zones.flavors..index)..index(data.cloudru_k8s_zone_flavors.k8s_zones.flavors..index)+1]
  }
  nodes_network_configuration = {
    nodes_subnet_cidr = "192.168.123.0/24"
  }
  depends_on = [
    cloudru_k8s_cluster.kube
  ]
}
```

С помощью этой конфигурации вы создадите новые ресурсы:
• Кластер Managed Kubernetes на базе одного мастер-узла.
• Одну группу узлов.

2. Сохраните файл kuber.tf.
3. В терминале перейдите в папку проекта и выполните команду:

```bash
terraform validate
```

4. Если все прошло успешно, вы увидите похожий текст:

```
Success! The configuration is valid.
```

При необходимости устраните ошибки в конфигурации.
5. Выполните команду:

```bash
terraform apply
```

6. Убедитесь, что Terraform планирует добавить два ресурса, введите «yes» и нажмите Enter.
Если развертывание прошло успешно, вы увидите следующее сообщение:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

3. Проверьте создание кластера и подключитесь к нему

1. Перейдите в личный кабинет Cloud.ru Evolution и проверьте, что все созданные ресурсы отображаются.

![Скриншот страницы с кластерами Managed Kubernetes](https://example.com/screenshot.png)

2. Подключитесь к кластеру и выполните команду:

```bash
kubectl cluster-info
```

Команда выведет информацию о вашем кластере.

Результат

Вы познакомились с механизмом развертывания облачных ресурсов Terraform и научились работать с инструментами в рамках концепции Infrastructure as Code.