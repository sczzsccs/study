using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    private void Awake() // 오브젝트 초기화
    {
        Debug.Log("준비 완료.");
    }

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Hi");

        string Name = "My name is...";
        Debug.Log(Name);

        List<string> State = new List<string>();
        State.Add("체력: " + 100);
        State.Add("마나: " + 50);
        State.Add("생명력: " + 10);
        State.Add("민첩성: " + 5);
        State.Add("회피력:" + 3);

        Debug.Log("------캐릭터 상태--------------");
        for (int i = 0; i < State.Count; i++)
        {
            Debug.Log(State[i]);
        }
        //int health = 10;
        //health = Heal(health);
        Heal();
    }

    private void OnEnable() // 오브젝트 활성화 시
    {// 초기화 이후 오브젝트 활성화 때마다 실행
        Debug.Log("로그인.");
    //물리연산 전 실행
    }

    private void FixedUpdate() // 물리연산 전 업데이트
    {// 업데이트: 초당 프레임(FPS) 고정된 주기로 실행
     // CPU부하
        Debug.Log("이동~");
    }

    private void Update() // 주기적으로 변해야 할 경우
    {// ※환경에 따라 실행주기가 달라질 수 있음
        Debug.Log("몬스터 사냥!!");
    }

    private void LateUpdate() // 모든 업데이트가 끝난 후
    {// 로직의 후 처리, 카메라 등
        Debug.Log("경험치 획득.");
    }

    private void OnDisable() // 오브젝트 비활성화 시
    {// 로직처리 이후, 비활성화 때마다 실행
        Debug.Log("로그아웃.");
     // 오브젝트가 삭제되기 전 실행        
    }
    private void OnDestroy() // 오브젝트가 삭제될 때
    {
        Debug.Log("삭제완료.");
    }

    int Heal(int Health)
    {
        Health += 10;
        Debug.Log("힐을 받았습니다. " + Health);
        return Health;
    } 
    int health = 30;

    void Heal()
    {
        this.health += 10;
        Debug.Log("힐을 받았습니다. " + health);
    }

    // 클래스
    Acter Player = new Acter();

/*    // Update is called once per frame
    void Update()
    {

    }*/
}
