using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class NewBehaviourScript1 : MonoBehaviour
{
    // Initialization
    private void Awake() 
    {
        Debug.Log("������Ʈ ����.");
    }

    private void OnEnable() // ������Ʈ Ȱ��ȭ ��
    {
        Debug.Log("������Ʈ Ȱ��ȭ");
    }

    private void Start()
    {
        Debug.Log("������Ʈ ���۽��� \nŰ�� �Է��ϼ���.");
    }

    private float JumpSpeed = 0;
    private int JumpHigh = 0;
    private string State = "";

    // Update is called once per frame
    void Update()
    {
        float XPos, ZPos;
        string pos_str;

        XPos = Input.GetAxis("Horizontal");
        ZPos = Input.GetAxis("Vertical");

        if (Input.GetButton("Horizontal")) {
            switch (Input.GetAxisRaw("Horizontal") + 2)
            {
                case 1: pos_str = "Left";
                    break;
                case 2: pos_str = "Mid";
                    break;
                default: pos_str = "Right";
                    break;
            }
            Debug.Log("���� �̵�.\n" 
                + "��ǥ:" + XPos + "\n"
                + pos_str);
        }
        else if (Input.GetButton("Vertical"))
        {
            switch (Input.GetAxisRaw("Vertical") + 2)
            {
                case 1:
                    pos_str = "Dwon";
                    break;
                case 2:
                    pos_str = "Mid";
                    break;
                default:
                    pos_str = "Up";
                    break;
            }
            Debug.Log("���� �̵�.\n"
                + "��ǥ:" + ZPos + "\n"
                + pos_str);
        };

        if ((Input.GetKey(KeyCode.Space)) && (State != "Down")) {
            State = "Jump"; }
        else if (Input.GetKeyUp(KeyCode.Space))
        {
            State = "Down"; }

        if (State == "Jump")
        {
            JumpHigh ++;
            JumpSpeed = (float)0.15;
            if (JumpHigh >= 45) { 
                JumpSpeed = 0;
                State = "Down";
            }
            Debug.Log("Jump:" + JumpHigh
                + "\nJumpSpeed" + JumpSpeed);
        }
        else if (State == "Down")
        {
            if (JumpHigh == 0)
            {
                JumpSpeed = 0;
                JumpHigh = 0;
                State = "Non";
            }
            else if (JumpHigh > 0)
            {
                JumpHigh --;
                JumpSpeed = (float)-0.15;
            }
            Debug.Log("Jump:" + JumpHigh
                + "\nJumpSpeed" + JumpSpeed);
        }

        XPos /= 10;
        ZPos /= 10;
        transform.Translate(
            new Vector3(
                x: XPos,
                y: JumpSpeed,
                z: ZPos));
    }

    private void FixedUpdate()
    {
        
    }
}
