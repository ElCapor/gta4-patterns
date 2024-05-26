mov eax, 0x2C ;
push 0
mov eax, [eax]
push 10
mov ecx, [eax+8]
push 0x1C
mov eax, [ecx]
call dword ptr [eax+8]