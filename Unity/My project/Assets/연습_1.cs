using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    private void Awake() // ������Ʈ �ʱ�ȭ
    {
        Debug.Log("�غ� �Ϸ�.");
    }

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Hi");

        string Name = "My name is...";
        Debug.Log(Name);

        List<string> State = new List<string>();
        State.Add("ü��: " + 100);
        State.Add("����: " + 50);
        State.Add("�����: " + 10);
        State.Add("��ø��: " + 5);
        State.Add("ȸ�Ƿ�:" + 3);

        Debug.Log("------ĳ���� ����--------------");
        for (int i = 0; i < State.Count; i++)
        {
            Debug.Log(State[i]);
        }
        //int health = 10;
        //health = Heal(health);
        Heal();
    }

    private void OnEnable() // ������Ʈ Ȱ��ȭ ��
    {// �ʱ�ȭ ���� ������Ʈ Ȱ��ȭ ������ ����
        Debug.Log("�α���.");
    //�������� �� ����
    }

    private void FixedUpdate() // �������� �� ������Ʈ
    {// ������Ʈ: �ʴ� ������(FPS) ������ �ֱ�� ����
     // CPU����
        Debug.Log("�̵�~");
    }

    private void Update() // �ֱ������� ���ؾ� �� ���
    {// ��ȯ�濡 ���� �����ֱⰡ �޶��� �� ����
        Debug.Log("���� ���!!");
    }

    private void LateUpdate() // ��� ������Ʈ�� ���� ��
    {// ������ �� ó��, ī�޶� ��
        Debug.Log("����ġ ȹ��.");
    }

    private void OnDisable() // ������Ʈ ��Ȱ��ȭ ��
    {// ����ó�� ����, ��Ȱ��ȭ ������ ����
        Debug.Log("�α׾ƿ�.");
     // ������Ʈ�� �����Ǳ� �� ����        
    }
    private void OnDestroy() // ������Ʈ�� ������ ��
    {
        Debug.Log("�����Ϸ�.");
    }

    int Heal(int Health)
    {
        Health += 10;
        Debug.Log("���� �޾ҽ��ϴ�. " + Health);
        return Health;
    } 
    int health = 30;

    void Heal()
    {
        this.health += 10;
        Debug.Log("���� �޾ҽ��ϴ�. " + health);
    }

    // Ŭ����
    Acter Player = new Acter();

/*    // Update is called once per frame
    void Update()
    {

    }*/
}
