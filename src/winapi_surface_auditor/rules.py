"""Risky Windows API usage rules for defensive code review."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    api: str
    category: str
    severity: str
    why: str
    safer: str

RULES = [
    Rule("VirtualAllocEx", "cross-process memory", "high",
         "Allocates memory in another process; a classic injection primitive.",
         "Prefer in-process allocation; if cross-process work is required, document the trust boundary."),
    Rule("WriteProcessMemory", "cross-process memory", "high",
         "Writes into another process's memory space.",
         "Use documented IPC (pipes, RPC, shared memory with ACLs) instead."),
    Rule("CreateRemoteThread", "cross-process execution", "high",
         "Starts a thread in another process.",
         "Use supported plug-in/extension models or same-process threading."),
    Rule("NtCreateThreadEx", "cross-process execution", "high",
         "Low-level remote thread creation, often used to bypass monitoring.",
         "Use CreateThread for own-process work; justify any Nt* usage."),
    Rule("SetWindowsHookEx", "input interception", "medium",
         "Global hooks can observe input across processes.",
         "Scope hooks to your own thread/process where possible."),
    Rule("GetAsyncKeyState", "input interception", "medium",
         "Polls global key state; keylogging-capable pattern.",
         "Handle input through your own window messages."),
    Rule("ShellExecute", "process creation", "low",
         "Launches programs/documents; risky with unvalidated input.",
         "Validate and quote arguments; prefer CreateProcess with explicit args."),
    Rule("WinExec", "process creation", "medium",
         "Legacy process launch with weak argument handling.",
         "Use CreateProcess with a fixed application path."),
    Rule("CryptEncrypt", "cryptography", "low",
         "Legacy CryptoAPI usage; check algorithm and key handling.",
         "Prefer BCrypt/NCrypt with authenticated modes (AES-GCM)."),
    Rule("IsDebuggerPresent", "anti-analysis", "low",
         "Debugger check; legitimate in licensing, suspicious elsewhere.",
         "Keep anti-tamper checks documented and proportionate."),
]
RULE_BY_API = {r.api: r for r in RULES}
