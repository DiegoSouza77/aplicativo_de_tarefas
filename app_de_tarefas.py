# app_de_tarefas.py

class App:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            status = '✔️' if task['completed'] else '❌'
            print(f"{index + 1}. {task['task']} - {status}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
        else:
            print("Índice de tarefa inválido")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Índice de tarefa inválido")

def main():
    app = ToDoApp()
    while True:
        print("\nOpções:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Excluir tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa: ")
            app.add_task(task)
        elif choice == '2':
            app.list_tasks()
        elif choice == '3':
            task_index = int(input("Digite o número da tarefa a marcar como concluída: ")) - 1
            app.complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Digite o número da tarefa a excluir: ")) - 1
            app.delete_task(task_index)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
