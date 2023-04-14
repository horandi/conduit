import { Buffer } from "./buffer.ts";
const DEFAULT_BUFFER_SIZE = 32 * 1024;
export async function readAll(r) {
    const buf = new Buffer();
    await buf.readFrom(r);
    return buf.bytes();
}
export function readAllSync(r) {
    const buf = new Buffer();
    buf.readFromSync(r);
    return buf.bytes();
}
export async function writeAll(w, arr) {
    let nwritten = 0;
    while (nwritten < arr.length) {
        nwritten += await w.write(arr.subarray(nwritten));
    }
}
export function writeAllSync(w, arr) {
    let nwritten = 0;
    while (nwritten < arr.length) {
        nwritten += w.writeSync(arr.subarray(nwritten));
    }
}
export async function* iter(r, options) {
    const bufSize = options?.bufSize ?? DEFAULT_BUFFER_SIZE;
    const b = new Uint8Array(bufSize);
    while (true) {
        const result = await r.read(b);
        if (result === null) {
            break;
        }
        yield b.subarray(0, result);
    }
}
export function* iterSync(r, options) {
    const bufSize = options?.bufSize ?? DEFAULT_BUFFER_SIZE;
    const b = new Uint8Array(bufSize);
    while (true) {
        const result = r.readSync(b);
        if (result === null) {
            break;
        }
        yield b.subarray(0, result);
    }
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoidXRpbC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbInV0aWwudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsT0FBTyxFQUFFLE1BQU0sRUFBRSxNQUFNLGFBQWEsQ0FBQztBQUVyQyxNQUFNLG1CQUFtQixHQUFHLEVBQUUsR0FBRyxJQUFJLENBQUM7QUFzQnRDLE1BQU0sQ0FBQyxLQUFLLFVBQVUsT0FBTyxDQUFDLENBQWM7SUFDMUMsTUFBTSxHQUFHLEdBQUcsSUFBSSxNQUFNLEVBQUUsQ0FBQztJQUN6QixNQUFNLEdBQUcsQ0FBQyxRQUFRLENBQUMsQ0FBQyxDQUFDLENBQUM7SUFDdEIsT0FBTyxHQUFHLENBQUMsS0FBSyxFQUFFLENBQUM7QUFDckIsQ0FBQztBQXFCRCxNQUFNLFVBQVUsV0FBVyxDQUFDLENBQWtCO0lBQzVDLE1BQU0sR0FBRyxHQUFHLElBQUksTUFBTSxFQUFFLENBQUM7SUFDekIsR0FBRyxDQUFDLFlBQVksQ0FBQyxDQUFDLENBQUMsQ0FBQztJQUNwQixPQUFPLEdBQUcsQ0FBQyxLQUFLLEVBQUUsQ0FBQztBQUNyQixDQUFDO0FBc0JELE1BQU0sQ0FBQyxLQUFLLFVBQVUsUUFBUSxDQUFDLENBQWMsRUFBRSxHQUFlO0lBQzVELElBQUksUUFBUSxHQUFHLENBQUMsQ0FBQztJQUNqQixPQUFPLFFBQVEsR0FBRyxHQUFHLENBQUMsTUFBTSxFQUFFO1FBQzVCLFFBQVEsSUFBSSxNQUFNLENBQUMsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLFFBQVEsQ0FBQyxRQUFRLENBQUMsQ0FBQyxDQUFDO0tBQ25EO0FBQ0gsQ0FBQztBQXVCRCxNQUFNLFVBQVUsWUFBWSxDQUFDLENBQWtCLEVBQUUsR0FBZTtJQUM5RCxJQUFJLFFBQVEsR0FBRyxDQUFDLENBQUM7SUFDakIsT0FBTyxRQUFRLEdBQUcsR0FBRyxDQUFDLE1BQU0sRUFBRTtRQUM1QixRQUFRLElBQUksQ0FBQyxDQUFDLFNBQVMsQ0FBQyxHQUFHLENBQUMsUUFBUSxDQUFDLFFBQVEsQ0FBQyxDQUFDLENBQUM7S0FDakQ7QUFDSCxDQUFDO0FBK0JELE1BQU0sQ0FBQyxLQUFLLFNBQVMsQ0FBQyxDQUFDLElBQUksQ0FDekIsQ0FBYyxFQUNkLE9BRUM7SUFFRCxNQUFNLE9BQU8sR0FBRyxPQUFPLEVBQUUsT0FBTyxJQUFJLG1CQUFtQixDQUFDO0lBQ3hELE1BQU0sQ0FBQyxHQUFHLElBQUksVUFBVSxDQUFDLE9BQU8sQ0FBQyxDQUFDO0lBQ2xDLE9BQU8sSUFBSSxFQUFFO1FBQ1gsTUFBTSxNQUFNLEdBQUcsTUFBTSxDQUFDLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQyxDQUFDO1FBQy9CLElBQUksTUFBTSxLQUFLLElBQUksRUFBRTtZQUNuQixNQUFNO1NBQ1A7UUFFRCxNQUFNLENBQUMsQ0FBQyxRQUFRLENBQUMsQ0FBQyxFQUFFLE1BQU0sQ0FBQyxDQUFDO0tBQzdCO0FBQ0gsQ0FBQztBQStCRCxNQUFNLFNBQVMsQ0FBQyxDQUFDLFFBQVEsQ0FDdkIsQ0FBa0IsRUFDbEIsT0FFQztJQUVELE1BQU0sT0FBTyxHQUFHLE9BQU8sRUFBRSxPQUFPLElBQUksbUJBQW1CLENBQUM7SUFDeEQsTUFBTSxDQUFDLEdBQUcsSUFBSSxVQUFVLENBQUMsT0FBTyxDQUFDLENBQUM7SUFDbEMsT0FBTyxJQUFJLEVBQUU7UUFDWCxNQUFNLE1BQU0sR0FBRyxDQUFDLENBQUMsUUFBUSxDQUFDLENBQUMsQ0FBQyxDQUFDO1FBQzdCLElBQUksTUFBTSxLQUFLLElBQUksRUFBRTtZQUNuQixNQUFNO1NBQ1A7UUFFRCxNQUFNLENBQUMsQ0FBQyxRQUFRLENBQUMsQ0FBQyxFQUFFLE1BQU0sQ0FBQyxDQUFDO0tBQzdCO0FBQ0gsQ0FBQyJ9