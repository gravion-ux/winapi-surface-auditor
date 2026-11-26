from winapi_surface_auditor.scanner import scan_text, summarise

SAMPLE = """
#include <windows.h>
int main() {
    HANDLE h = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    LPVOID mem = VirtualAllocEx(h, NULL, 4096, MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(h, mem, buf, 4096, NULL);
    CreateThread(NULL, 0, worker, NULL, 0, NULL);
    return 0;
}
"""

def test_detects_cross_process_apis():
    apis = {f.api for f in scan_text(SAMPLE)}
    assert "VirtualAllocEx" in apis
    assert "WriteProcessMemory" in apis

def test_own_process_thread_not_flagged():
    assert all(f.api != "CreateThread" for f in scan_text(SAMPLE))

def test_line_numbers():
    findings = scan_text(SAMPLE)
    va = next(f for f in findings if f.api == "VirtualAllocEx")
    assert va.line == 5

def test_summary_counts():
    s = summarise(scan_text(SAMPLE))
    assert s["by_severity"]["high"] == 2
    assert s["total"] == 2

def test_clean_code_no_findings():
    assert scan_text("int add(int a, int b) { return a + b; }") == []
